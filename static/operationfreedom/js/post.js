$(document).ready(function(){



  


  
})












// $.ajax({
//   type:'GET',
//   url: 'post/<int:pk>/',
//   success: function(response){
//     console.log(response.parent_comment)
//   },
//   error: function(error){
//     console.log(error)
//   }
// });











// $(document).ready(function(){
//   $.ajax({
//       type:'GET',
//       url: 'post/<int:pk>/',
//       success: function(response){
//           // console.log(response.comment)
//           const comment = response.comment
//           comment.map(post=>{
//               console.log(post.pk)
//           })
//       },
//       error: function(error){
//           console.log(error)
//       }
//   })
// })













// $(document).ready(function(){
//   var limit=10;
//   var start=0;
//   var action='inactive'
//   function load_post_data(limit, start){
//     $.ajax({
//       url:'get-post-list/',
//       method:'GET',
//       data:{
//         limit:limit,
//         start:start
//       },
//       caches:false,
//       success:function(response){
//         $("#post-container").append(response);
//         if(response==0){
//           $('#more-data').html("<button type='button' class='btn btn-info'>No More Posts</button>", action='active')
//         }else{
//           $('#more-data').html("<button type='button' class='btn btn-info'>Loading more posts....</button>", action='inactive')
//         }
//       }
//     })
//   }
//   if(action=='inactive'){
//     action='active',
//     load_post_data(limit, start)
//   }
//   $(window).scroll(function(){
//   	if($(window).scrollTop() +$(window).height() > $('#post-container').height() && action =='inactive'){
//   		action='active';
//   		start=start + limit;
//   		setTimeout(function(){
//   			load_post_data(limit, start);
//   		}, 1000)
//   	}
//   })
// })




// $(document).ready(function(){
//   var limit=10;
//   var start=0;
//   var action='inactive'
//   function load_post_data(limit, start){
//     $.ajax({
//       url:'with-posts/',
//       method:'GET',
//       data:{
//         limit:limit,
//         start:start
//       },
//       caches:false,
//       success:function(response){
//         $("#profile-post-container").append(response);
//         if(response==0){
//           $('#profile-more-data').html("<button type='button' class='btn btn-info'>No More Posts</button>", action='active')
//         }else{
//           $('#profile-more-data').html("<button type='button' class='btn btn-info'>Loading more posts....</button>", action='inactive')
//         }
//       }
//     })
//   }
//   if(action=='inactive'){
//     action='active',
//     load_post_data(limit, start)
//   }
//   $(window).scroll(function(){
//   	if($(window).scrollTop() +$(window).height() > $('#profile-post-container').height() && action =='inactive'){
//   		action='active';
//   		start=start + limit;
//   		setTimeout(function(){
//   			load_post_data(limit, start);
//   		}, 1000)
//   	}
//   })
// })







// $(document).ready(function(){
//   var limit=10;
//   var start=0;
//   var action='inactive'
//   function load_post_data(limit, start){
//     $.ajax({
//       url:'with-commentss/',
//       method:'GET',
//       data:{
//         limit:limit,
//         start:start
//       },
//       caches:false,
//       success:function(response){
//         $("#comments-container").append(response);
//         if(response==0){
//           $('#comments-more-data').html("<button type='button' class='btn btn-info'>No More Posts</button>", action='active')
//         }else{
//           $('#comments-more-data').html("<button type='button' class='btn btn-info'>Loading more posts....</button>", action='inactive')
//         }
//       }
//     })
//   }
//   if(action=='inactive'){
//     action='active',
//     load_post_data(limit, start)
//   }
//   $(window).scroll(function(){
//   	if($(window).scrollTop() +$(window).height() > $('#comments-container').height() && action =='inactive'){
//   		action='active';
//   		start=start + limit;
//   		setTimeout(function(){
//   			load_post_data(limit, start);
//   		}, 1000)
//   	}
//   })
// })


