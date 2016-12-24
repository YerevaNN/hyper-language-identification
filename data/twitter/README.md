These data are from [Mitja Trampus](https://github.com/mitjat)'s [language identification evaluation](https://github.com/mitjat/langid_eval/)

For the full write-up, see [Evaluating language identification performance | Twitter Blogs](https://blog.twitter.com/2015/evaluating-language-identification-performance).

The complete steps for getting the data are described there.  To get started:

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
