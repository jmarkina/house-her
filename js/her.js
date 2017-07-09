

var story_data = storydata;
 
for (var key in story_data){
    // loop over all stories and save to div

    var allStories;
    allStories = "<div class='each-story'> " + story_data[key].story + "</div>";
    document.write(allStories);
};

