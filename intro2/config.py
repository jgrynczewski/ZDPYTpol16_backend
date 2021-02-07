class Config:

    def get(self, key):
        with open('tags', 'r') as f:
            tags = f.readlines()[:-1]

        for item in tags:
            pairs = item.split("=")
            if pairs[0]==key:
                return pairs[1]
            else:
                return ""