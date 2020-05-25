import http.client

conn = http.client.HTTPSConnection("quillbot.p.rapidapi.com")

payload = "{\t\"text\":\"Researchers in the field of HCI both observe the ways in which humans interact with computers and design technologies that let humans interact with computers in novel ways. Humans interact with computers in many ways; the interface between humans and computers is crucial to facilitating this interaction.\",\t\"numParaphrases\":1,\t\"coupon\":\"IJg98DCuPqGuit7BrGXKaWsoqOUz0DYV\",  \"includeSegs\":true,\"strength\":3,\"autoflip\":0.25}"

headers = {
    'x-rapidapi-host': "quillbot.p.rapidapi.com",
    'x-rapidapi-key': "dd36383ff6msh984b1f8a7b82d0bp1e31bbjsna31133dc74f6",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/paraphrase", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))