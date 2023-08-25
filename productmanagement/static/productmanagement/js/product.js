function getCategoryCodeByAjax(thisobj){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
	var get_category_ajax_url = $("#get_category_ajax_url").val();
	var cat_id = thisobj.value;
     $.ajaxSetup({
            headers: {
                "X-CSRFToken": csrftoken,
            }
     });  	
	 $.ajax({
	   type : 'POST',
	   url : get_category_ajax_url,
	   data : {cat_id:cat_id},
	   success : function(res){
	         var catcode = res.catcode;
			
			$("#catcode").val(catcode);
	    },
	 
	 });

}