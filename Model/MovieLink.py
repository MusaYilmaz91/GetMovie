class MovieLink:
    def __init__(self, id:int, url:str):
        self.LinkId =id
        self.Link=url
        
    def to_dict(self):
        return {
            "Link_id": self.LinkId,
            "Link": self.Link,
        }