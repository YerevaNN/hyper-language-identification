These data are from Twitter's [Evaluating language identification performance](https://blog.twitter.com/2015/evaluating-language-identification-performance).

#### Getting started

The complete steps for getting the data are described at [Mitja Trampus](https://github.com/mitjat)'s [language identification evaluation](https://github.com/mitjat/langid_eval/) repo README.

0 - Make a virtual env (optional but recommended)

    virtualenv tmpenv
    source tmpenv/bin/activate

1 - Install python-twitter

    pip install -r requirements.txt 

2 - Set [Twitter OAuth credentials](https://apps.twitter.com/app/new)

    export TWITTER_API_KEY=<your-key>
    export TWITTER_API_SECRET=<your-secret>    
    export TWITTER_API_ACCESS_TOKEN=<your-API-access-token-key>
    export TWITTER_API_ACCESS_TOKEN_SECRET=<your-API-access-token-secret>  

3 - Get the actual text data for the provided list of Tweet ids and language labels

    python lookup.py uniformly_sampled.tsv

You should now have a file `uniformly_sampled.tsv.json`.

If for some reason it is interrupted, you can restart at a specific record:

    python lookup.py uniformly_sampled.tsv <status_id>
    