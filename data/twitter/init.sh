cat >/tmp/fetch.sh <<'EOF'
#!/bin/bash
sleep 5
twurl "/1.1/statuses/lookup.json?id=$(echo $@ | tr ' ' ,)&trim_user=true" | jq -c ".[]|[.id_str, .text]"
EOF

cat "$1" | cut -f2 | xargs -n100 /tmp/fetch.sh > "$1.json"
