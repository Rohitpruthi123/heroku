mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"pruthirohit@outlook.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
enableCORS=false
headless = true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml