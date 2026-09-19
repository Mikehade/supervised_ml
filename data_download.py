import kagglehub

# Download latest version
path = kagglehub.competition_download('playground-series-s4e1')

print("Path to competition files:", path)