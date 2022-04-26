function commentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

function shareToggle(parent_id) {
	const row = document.getElementById(parent_id);

	if (row.classList.contains('d-none')) {
		row.classList.remove('d-none');
	} else {
		row.classList.add('d-none');
	}
}

function imageToggle(parent_id) {
	const row = document.getElementById(parent_id);

	if (row.classList.contains('k-none')) {
		row.classList.remove('k-none');
	} else {
		row.classList.add('k-none');
	}
}


// function repliesToggle() {
// 	const row = document.getElementById('commentreply');

// 	if (row.classList.contains('k-none')) {
// 		row.classList.remove('k-none');
// 	} else {
// 		row.classList.add('k-none');
// 	}
// }


function showNotifications() {
	const container = document.getElementById('notification-container');

	if (container.classList.contains('d-none')) {
		container.classList.remove('d-none');
	} else {
		container.classList.add('d-none');
	}
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function removeNotification(removeNotificationURL, redirectURL) {
	const csrftoken = getCookie('csrftoken');
	let xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == XMLHttpRequest.DONE) {
			if (xmlhttp.status == 200) {
				window.location.replace(redirectURL);
			} else {
				alert('There was an error');
			}
		}
	};

	xmlhttp.open("DELETE", removeNotificationURL, true);
	xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
	xmlhttp.send();
}

function formatTags() {
	const elements = document.getElementsByClassName('body');
	for (let i = 0; i < elements.length; i++) {
		let bodyText = elements[i].children[0].innerText;

		let words = bodyText.split(' ');

		for (let j = 0; j < words.length; j++) {
			if (words[j][0] === '#') {
				let replacedText = bodyText.replace(/\s\#(.*?)(\s|$)/g, ` <a href="/social/explore?query=${words[j].substring(1)}">${words[j]}</a>`);
				elements[i].innerHTML = replacedText;
			}
		}
	}
}

formatTags();









// tried to create load more button for replies 

// const repliesBox = document.getElementById('replies-box')
// console.log(repliesBox)
// const spinnerBox = document.getElementById('spinner-box')
// const loadBtn = document.getElementById('load-btn')
// const loadBox = document.getElementById('loading-box')
// const repliesBox = document.getElementsByClassName('replies-box');
// console.log(repliesBox)
// const spinnerBox = document.getElementsByClassName('spinner-box');
// const loadBtn = document.getElementsByClassName('load-btn');
// const loadBox = document.getElementsByClassName('loading-box');
// let visible = 3 

// const handleGetReplies = () => {
// 	$.ajax({
// 		type: 'GET',
// 		url: `post/<int:post_pk>/comment/<int:pk>/reply/${visible}/`,
// 		success: function(response){
// 			maxSize = response.max
// 			const data = response.data
// 			spinnerBox.classList.remove('not-visible')
// 			setTimeout(()=>{
// 				spinnerBox.classList.add('not-visible')

// 				data.map(comment.children=>{
// 					console.log(comment.children.pk)



// 					repliesBox.innerHTML += `{% for child_comment in comment.children %}
// 											<div class="row justify-content-center child-comment">
// 			                                    <div class="col-md-5 col-sm-12">
// 			                                        <div>
// 			                                            <a href="{% url 'show_profile_page' child_comment.author.profile.pk %}">
// 			                                                <img class="round-circle post-img" height="30" width="30" src="${ child_comment.author.profile.picture.url }"/>
// 			                                            </a>
// 			                                            <p class="post-text">
// 			                                                <a class="text-primary post-link" href="{% url 'show_profile_page' child_comment.author.profile.pk %}">@${ child_comment.author }</a> replied on {{ child_comment.created_on }}
// 			                                            </p>
// 			                                        </div>
// 			                                        {% if request.user == child_comment.author %}
// 			                                            <a href="{% url 'comment-delete' post.pk child_comment.pk %}" class="edit-color"><i class="fas fa-trash"></i></a>
// 			                                        {% endif %}
			                                        
// 			                                        <p>${ child_comment.comment }</p>
// 			                                    </div>
// 			                                </div>
// 			                                {% endfor %}`
// 				})
// 			}, 500)
// 			if(maxSize){
// 				console.log('done')
// 				loadBox.innerHTML = "<h4>No more posts to load</h4>"
// 			}
// 		},
// 		error: function(error){
// 			console.log(error)
// 		}
// 	})

// }

// handleGetReplies()
// loadBtn.addEventListener('click', ()=>{
//     visible += 3
//     handleGetReplies()
// })





