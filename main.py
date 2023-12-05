import pandas as pd
import receipt

df =  pd.read_csv("articles.csv", dtype={"id":str, "name":str, "price": str})


class Article:
    def __init__(self, article_id) -> None:
        self.article_id = article_id
        print("article id: ", article_id)
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.stock = df.loc[df["id"] == self.article_id, "stock"].squeeze()
        
    
    def available(self):
        if int(self.stock) > 0:
            return True
        return False


    def purchase(self):
        """Change the stock amount"""
        df.loc[df["id"] == self.article_id, "stock"] = int(self.stock) - 1
        df.to_csv("articles.csv", index=False)
    
    def receipt(self):
        """Print the receipt """
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()
        receipt.create_receipt(self.article_id, self.name, self.price)


if __name__ == "__main__":
    # List the items for sale
    print(df)
    article_id = input("Enter the id of the article you want to purchase: ")
    article = Article(article_id=article_id)

    # Check the availability of articles 
    print(article.purchase())
    if article.available():
        article.purchase()
        article.receipt()

