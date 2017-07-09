

var story_data = storydata;
 
for (var key in story_data){
    // loop over all stories and save to div

    var allStories;
    allStories = "<a href='full-story-" + key + ".html'><div class='short-story push-1-12 col-5-12 texture' id=" + key + ">" + story_data[key].story.substr(0,40) + "..." + "</div></a>";
    document.write(allStories);

};



