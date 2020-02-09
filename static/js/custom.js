function myFunction(clicked_id){
    
    $(document).ready(function(){
        url = '/listStudentsRandom.html';
        $(clicked_id).click(function(){
            $.ajax({
                url: url,
                type: "GET",
                success:function(result){
                    console.log(result)
                },
                error: function(error){
                    console.log('Error ${error}')
                }
            })
        })
    }
    
    )


}
