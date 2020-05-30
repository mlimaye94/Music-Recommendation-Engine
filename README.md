# Music-Recommendation-Engine

Dataset: Million Song Dataset ---> http://millionsongdataset.com/

Business Case Presentation: https://www.youtube.com/watch?v=eMkZwNPMyEY

The project aims at building a song recommendation engine for users given their listening history. We aim to
understand the user’s song preference using various features of the songs previously listened to by the user. Music streaming services could benefit from this approach as it gives them a platform to understand user behavior and recommend songs accordingly. Additionally, record labels and artists can perform targeted marketing for their newly released songs using data of users provided by the recommendation engine. Our project also aims at solving the ‘cold-start problem’ a prevalent issue in this space, by recommending new songs to the users given their previously listened songs.

One of the key aspects of our project is that it takes into consideration the lyrics of the songs to understand whether similarity in lyrics plays a role in a user’s song selection along with other song features. In order to achieve this, an NLP technique called topic modeling was performed that clustered the words into multiple groups and assigned topics to each group. Using these topics, the percentage contribution of each topic in a particular song listened was determined. The project aims to use these lyrics contributed features along with traditional song features and artist features to build a user profile for every user. This profile is used to understand user’s music taste and determine his likelihood to listen to a new song. This, in turn, forms the basis of our recommendation engine.

The project uses songs, lyrics, and user metadata from the Million Song Dataset. Corresponding train and test datasets were build using multiple iterative steps to ensure same users and different songs in both these sets. Feature engineering was performed using multiple aggregated statistics of user-song interaction and user profiles generated using past listening habits to determine the optimal features for classification. The likelihood of a user listening to a new new song was then analyzed using multiple classification models. Based on the structure of our experiment and evaluation matrix, we observed that the Decision Tree Classifier performed better than the rest of the models.
