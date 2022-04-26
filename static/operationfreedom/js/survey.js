 $(document).ready(function(){

  
// survey.0 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  //like ajax call
  $('.like-form0').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn0').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // survey.0
        if(response.liked===true){
          $('.like-icon0').addClass('btn-success')
        }else{
          $('.like-icon0').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon0").addClass("btn-success")
        }else{
          $(".dislike-icon0").removeClass("btn-success")
        }
        likes=$('#like_count0').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count0").text(response.dislikes_count)
        parseInt(dislikes)
      },                     
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike ajax call
  $('.dislike-form0').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn0").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon0").addClass("btn-success")
        }else{
          $(".dislike-icon0").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon0').addClass('btn-success')
        }else{
          $('.like-icon0').removeClass('btn-success')
        }
        likes=$('#like_count0').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count0").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });   



  // survey.1 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like ajax call
  $('.like-form1').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn1').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // survey.0
        if(response.liked===true){
          $('.like-icon1').addClass('btn-success')
        }else{
          $('.like-icon1').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon1").addClass("btn-success")
        }else{
          $(".dislike-icon1").removeClass("btn-success")
        }
        likes=$('#like_count1').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count1").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike1 ajax call
  $('.dislike-form1').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn1").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon1").addClass("btn-success")
        }else{
          $(".dislike-icon1").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon1').addClass('btn-success')
        }else{
          $('.like-icon1').removeClass('btn-success')
        }
       
        likes=$('#like_count1').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count1").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });   



  // survey.2 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like2 ajax call
  $('.like-form2').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn2').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon2').addClass('btn-success')
        }else{
          $('.like-icon2').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon2").addClass("btn-success")
        }else{
          $(".dislike-icon2").removeClass("btn-success")
        }
        likes=$('#like_count2').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count2").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike2 ajax call
  $('.dislike-form2').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn2").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon2").addClass("btn-success")
        }else{
          $(".dislike-icon2").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon2').addClass('btn-success')
        }else{
          $('.like-icon2').removeClass('btn-success')
        }
       
        likes=$('#like_count2').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count2").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.3 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like3 ajax call
  $('.like-form3').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn3').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon3').addClass('btn-success')
        }else{
          $('.like-icon3').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon3").addClass("btn-success")
        }else{
          $(".dislike-icon3").removeClass("btn-success")
        }
        likes=$('#like_count3').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count3").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike3 ajax call
  $('.dislike-form3').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn3").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon3").addClass("btn-success")
        }else{
          $(".dislike-icon3").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon3').addClass('btn-success')
        }else{
          $('.like-icon3').removeClass('btn-success')
        }
       
        likes=$('#like_count3').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count3").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.4 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like4 ajax call
  $('.like-form4').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn4').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon4').addClass('btn-success')
        }else{
          $('.like-icon4').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon4").addClass("btn-success")
        }else{
          $(".dislike-icon4").removeClass("btn-success")
        }
        likes=$('#like_count4').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count4").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike4 ajax call
  $('.dislike-form4').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn4").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon4").addClass("btn-success")
        }else{
          $(".dislike-icon4").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon4').addClass('btn-success')
        }else{
          $('.like-icon4').removeClass('btn-success')
        }
       
        likes=$('#like_count4').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count4").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.5 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like5 ajax call
  $('.like-form5').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn5').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon5').addClass('btn-success')
        }else{
          $('.like-icon5').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon5").addClass("btn-success")
        }else{
          $(".dislike-icon5").removeClass("btn-success")
        }
        likes=$('#like_count5').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count5").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike5 ajax call
  $('.dislike-form5').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn5").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon5").addClass("btn-success")
        }else{
          $(".dislike-icon5").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon5').addClass('btn-success')
        }else{
          $('.like-icon5').removeClass('btn-success')
        }
       
        likes=$('#like_count5').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count5").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.5 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like5 ajax call
  $('.like-form6').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn6').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon6').addClass('btn-success')
        }else{
          $('.like-icon6').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon6").addClass("btn-success")
        }else{
          $(".dislike-icon6").removeClass("btn-success")
        }
        likes=$('#like_count6').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count6").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike6 ajax call
  $('.dislike-form6').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn6").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon6").addClass("btn-success")
        }else{
          $(".dislike-icon6").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon6').addClass('btn-success')
        }else{
          $('.like-icon6').removeClass('btn-success')
        }
       
        likes=$('#like_count6').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count6").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.7 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like7 ajax call
  $('.like-form7').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn7').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon7').addClass('btn-success')
        }else{
          $('.like-icon7').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon7").addClass("btn-success")
        }else{
          $(".dislike-icon7").removeClass("btn-success")
        }
        likes=$('#like_count7').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count7").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike7 ajax call
  $('.dislike-form7').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn7").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon7").addClass("btn-success")
        }else{
          $(".dislike-icon7").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon7').addClass('btn-success')
        }else{
          $('.like-icon7').removeClass('btn-success')
        }
       
        likes=$('#like_count7').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count7").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  });    



  // survey.8 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like8 ajax call
  $('.like-form8').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn8').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon8').addClass('btn-success')
        }else{
          $('.like-icon8').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon8").addClass("btn-success")
        }else{
          $(".dislike-icon8").removeClass("btn-success")
        }
        likes=$('#like_count8').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count8").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike8 ajax call
  $('.dislike-form8').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn8").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon8").addClass("btn-success")
        }else{
          $(".dislike-icon8").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon8').addClass('btn-success')
        }else{
          $('.like-icon8').removeClass('btn-success')
        }
       
        likes=$('#like_count8').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count8").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  }); 



  // survey.9 !!!!!!!!!!!!!!!!!!!!!!!!!
  //like9 ajax call
  $('.like-form9').submit(function(e){
    e.preventDefault();
    const survey_id=$('.like-btn9').val();
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{'X-CSRFToken': token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        if(response.liked===true){
          $('.like-icon9').addClass('btn-success')
        }else{
          $('.like-icon9').removeClass('btn-success')
        }
        if(response.disliked===true){
          $(".dislike-icon9").addClass("btn-success")
        }else{
          $(".dislike-icon9").removeClass("btn-success")
        }
        likes=$('#like_count9').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count9").text(response.dislikes_count)
        parseInt(dislikes)
      },           
      error:function(response){
        console.log("Failed ", response)
      }
    })
  });
  //dislike9 ajax call
  $('.dislike-form9').submit(function(e){
    e.preventDefault()
    const survey_id=$(".dislike-btn9").val()
    const token=$('input[name=csrfmiddlewaretoken]').val() 
    const url =$(this).attr('action') 
    $.ajax({
      method:"POST",
      url:url,
      headers:{"X-CSRFToken": token},
      data:{
        'survey_id':survey_id
      },
      success:function(response){
        // console.log(response)
        if(response.disliked===true){
          $(".dislike-icon9").addClass("btn-success")
        }else{
          $(".dislike-icon9").removeClass("btn-success")
        }

        if(response.liked===true){
          $('.like-icon9').addClass('btn-success')
        }else{
          $('.like-icon9').removeClass('btn-success')
        }
       
        likes=$('#like_count9').text(response.likes_count)
        parseInt(likes)
        dislikes=$("#dislike_count9").text(response.dislikes_count)
        parseInt(dislikes)
        
      },
      error:function(response){
        console.log('failed', response)
      }
    }) 
  }); 





});