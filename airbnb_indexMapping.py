indexMapping = {
    "properties":{
        "id":{
            "type":"long"
        },
        "name":{
            "type":"text"
        },
        "host_id":{
            "type":"long"
        },
        "host_name":{
            "type":"text"
        },
        "neighbourhood_group":{
            "type":"text"
        },
        "neighbourhood":{
            "type":"text"
        },
        "DescriptionVector":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}