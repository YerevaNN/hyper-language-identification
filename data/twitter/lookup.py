import twitter, sys, os, time, csv, json

api = twitter.Api(consumer_key=os.environ["TWITTER_API_KEY"],
                  consumer_secret=os.environ["TWITTER_API_SECRET"],
                  access_token_key=os.environ["TWITTER_API_ACCESS_TOKEN"],
                  access_token_secret=os.environ["TWITTER_API_ACCESS_TOKEN_SECRET"])

def lookup(file_path, start_status_id):
    with open(file_path) as f, open(file_path + '.json', 'a', encoding='utf-8') as f2:
        i = 0
        for row in csv.reader(f, delimiter='\t'):
            language, status_id = row[0], row[1]
            if not start_status_id or status_id == start_status_id:
                start_status_id = None
                while True:
                    try:
                        d = api.GetStatus(status_id).AsDict()
                        d.update({'true_language': language})
                        print(language, status_id, "READ")
                        f2.write(json.dumps(d, ensure_ascii=False))
                    except Exception as e:
                        print(language, status_id, e)
                        print(e.message[0]['message'])
                        if 'Rate limit exceeded' == e.message[0]['message']:
                            time.sleep(60)
                        else:
                            break


"""
    Hydrates a list of the format:
    
        <language_id>   <status_id>

    For example: 

        python lookup.py uniformly_sampled.tsv
        
    It will output uniformly_sampled.tsv.json of the format:
    
        {
            <status_id>:
                {
                    "true_language": <language_id>
                    "id": <status_id>
                    "language": <detected_language>
                    "time": ...
                    "location:" ...
                },
            ...
        }
    
"""
lookup(sys.argv[1], sys.argv[2])