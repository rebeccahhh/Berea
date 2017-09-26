console.log("javascript successfully accessed");
var app = new Vue({
	el: '#app',
	//App methods
	methods: {
		//add food to ingredients list
		add_food: function(){
			var ingredient = $("#ingredients").val();
			$("#ingredients").val("");
			this.$data.food_list.push({text:ingredient, url:"&allowedIngredient[]="+encodeURIComponent(ingredient)}); //create each list item with it's visual text component and URL section to be added to the API call later.
		},
		//Remove food from ingredients list
		remove_food: function(item){
			this.$data.food_list.splice(this.$data.food_list.indexOf(item), 1);
		},
		//API call to Yummly API, using the ingredients list as search parameters.
		search: function(){
			var param = ""
			$.each(this.$data.food_list, function(){
				param += this.url;
			});
			//API URL
			var temp = this;
			var url = "http://api.yummly.com/v1/api/recipes?_app_id=" + this.$data.app_id + "&_app_key=" + this.$data.app_key + param;
			$.get(url, function(response){
					temp.$data.recipe_list=response.matches;
					console.log(response);
				}
			);
		}
	},
	//App data
	data: {
    	header: "Fork Yeah!",
    	app_id: "609fe1cc",
    	app_key: "3a13c2bc8e1f1070d863c77b0526ddcc", // redact app key when pushing to git.
    	food_list: [],
    	recipe_list: []
  	}
});