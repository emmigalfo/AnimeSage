# AnimeSage
Personalized Anime Recommendation System
![Photo of recommender app](photos/AnimeSage.jpg)
## Project Overview
Anime Sage navigates through the extensive anime universe to deliver tailored recommendations to users. Utilizing data from My Anime List, the project developed a recommendation system that aligns with user preferences by employing an SVD model, achieving an RMSE of 1.16. The system is complemented by a user interface, enabling users to rate anime and receive immediate recommendations. While the current model effectively guides users to suitable anime titles, future iterations aim to explore hybrid models to further refine and personalize recommendations. Anime Sage strives to enhance user experience in anime exploration by continually evolving in its recommendation approach.
## Business Problem
There has been a surge in anime's popularity, not only in Japan but globally. Anime is becoming more promenent in consumer culture for both children and adults[^1^].Given the escalating interest and consumption of anime, there is a burgeoning need for sophisticated recommendation systems to navigate through the expansive anime domain, ensuring users can efficiently discover content that aligns with their preferences and enhances their engagement with the medium[^2^].
This project, born from my own challenges to find useful anime recommendations, aims to simplify this journey by developing a precise recommendation system tailored to individual preferences. In the booming anime industry, this system serves dual purposes: guiding viewers to titles they'll love and providing streaming platforms with a tool to enhance user engagement and potentially increase revenue through personalized content suggestions. The goal is to enrich the anime discovery and viewing experience, creating a win-win scenario for both viewers and streaming platforms by facilitating more personalized and satisfying content exploration.
## Data Understanding
The recommendation system is built upon data derived from My Anime List, a well-known online platform that provides its users with a comprehensive database of anime, including user ratings, reviews, and recommendations. The datasets utilized for this project can be accessed and reviewed [here](https://github.com/Hernan4444/MyAnimeList-Database). The files used were the anime.csv and rating_complete.csv files within the data folder.

- **Anime Data (`anime.csv`):** This dataset provides a detailed overview of various anime titles available on the platform. It encompasses numerous attributes such as anime ID, name, genre, type (e.g., TV, movie), episodes, rating, and members, among others.
- **User Ratings Data (`rating_complete.csv`):** This dataset includes the user interaction with various anime titles, represented through user IDs, anime IDs, and the respective ratings assigned by the users

## Exploratory Data Analysis
### Numerical Data
![heatmap of numerical correlation](photos/correlation_heatmap.png)
__Insights:__
There are quite a few features that show strong correlations. Lets look more closely at them.
* Score was highly negatively correlated with ranking. This is because ranking is determined by the score (with the exception of rated R18+ not being included in rankings)
* Popularity and ranking are highly correlated. The higher the ranking the more likely people are to have seen it.
* Members and Completed are very highly correlated. It follows that the more people have completed the show, the more members have it on their list.
* It also follows that the more people have the show marked on their list, the more people will have it tagged as 'plan to watch' as well as a higher score of 6-10. It goes along with the idea that the higher scored shows would be watched or planned to watch.
* Favorites also is highly correlated with the higher score columns which is expected. 
* The score columns (1-10) tend to highly correlate with the numerical score column directly above and directly below them. For example score-9 highly correlates with score-8 and score-10 but not with score-4. This makes sense overall a show will score within a certain range.
![user ratings](photos/distribution_user_ratings.png)

### Categorical Data
![Word cloud of categorical data](photos/wordcloud.png)
![squarify](photos/squarify.png)
![piechart](photos/ratingchart.png)
__Insights:__
1. It should come to no surprise for anime lovers that comedy was by far the most listed genre followed by action.
2. Toei Animation dominated in terms of studios with the most anime listed.  
3. Most anime was rated either PG-13, or G.




[^1^]Aziz, M., & Ong, S. (2023). The Implementation of Japanese Animation (Anime) In Advertising. Retrieved from https://jiss.publikasiindonesia.id/index.php/jiss/article/download/810/1524.
[^2^]Cho, H., Schmalz, M. L., Keating, S., & Lee, J. H. (2017). Information Needs for Anime Recommendation: Analyzing Anime Users' Online Forum Queries. In Proceedings of the 2017 ACM/IEEE Joint Conference on Digital Libraries (JCDL '17). DOI: 10.1109/JCDL.2017.7991602.
