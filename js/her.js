

var story_data = storydata;
 
for (var key in story_data){
    // loop over all stories and save to div
<<<<<<< HEAD
    console.log(story+key);
    // $('#story' + key).append(story_data[key].story);
    var new_story = console.log(story_data[key].story);
    console.log(key);

}





=======
    var allStories;
    allStories = "<div class='each-story'> " + story_data[key].story + "</div>";
    console.log(allStories);
    document.write(allStories);
};
>>>>>>> c6a079b7205700aebe78b4514f45c24af53f81fb

