

var story_data = storydata;
 
for (var key in story_data){
    // loop over all stories and save to div

    var allStories;
    allStories = "<div class='short-story' id=" + key + "><a href='full-story-" + key + ".html'></a>" + story_data[key].story.substr(0,40) + "..." + "</div>";
    document.write(allStories);
};



