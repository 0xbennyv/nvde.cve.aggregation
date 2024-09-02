# NVE CVE Compiler/Aggregator
I've have the need to query large amounts of CVE data and I've been hitting the rate limit on the NVE API.

As a result I've decided to just use the [CVEProject Git Repo](https://github.com/CVEProject/cvelistV5) then aggregate it to a single source. 

I tried cloning the local repo and use the folder structure in the repo but it was slow. I then tried to chuck it in a JSON file because it's quick and easy, but JSON isn't a database and also was far too slow. 

So I've got compile_to_sqlite.py which will create a sqlitedb with all the cve data and then query_sqlite.py which is an example to query the dataset.

I hope this helps a random internet user one day.