These data are from [Mitja Trampus](https://github.com/mitjat)'s [language identification evaluation](https://github.com/mitjat/langid_eval/)

For the full write-up, see [Evaluating language identification performance | Twitter Blogs](https://blog.twitter.com/2015/evaluating-language-identification-performance).

The complete steps for getting the data are described there.  To get started:

1 - Install twurl and jq

```
    sudo gem install twurl
    pip install jq
```

2 - Get [Twitter OAuth credentials](https://apps.twitter.com/app/new) and 
```
% twurl authorize --consumer-key <your-key>       \
                    --consumer-secret <your-secret>
```

3 - Get the actual text data for the provided list of Tweet ids and language labels
```
sh init.sh uniformly_sampled.tsv
```
You should now have a file `uniformly_sampled.tsv.json`.

