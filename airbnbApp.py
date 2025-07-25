import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "airbnb_properties"

try:
    es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "N*toUYVx44I4oLt5Sx4B"),
    ca_certs="/Users/avinashsrirama/Documents/Softwares/elasticsearch-8.18.4/config/certs/http_ca.crt",
    )
    
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")




def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DescriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index="airbnb_properties"
                        , knn=query 
                        , source=["name","neighbourhood_group"]
                        )
    results = res["hits"]["hits"]

    return results

def main():
    st.title("Search Airbnb Properties")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['name']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"City: {result['_source']['neighbourhood_group']}")
                        except Exception as e:
                            print(e)
                        st.divider()

                    
if __name__ == "__main__":
    main()
