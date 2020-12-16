
window.addEventListener('DOMContentLoaded', (event) => {
const all_todos = document.querySelectorAll('.delete_todo');
const todos_father = document.getElementById('todos_father');
  $(".delete_todo").click(function(event){
    let data_id = event.target.getAttribute('data-todo-id');

    $.ajax({
      type: 'POST',
      url: "/delete_todo",
      data: {todo_id: data_id},
      dataType: "text",
      success: function(data){

var y = document.querySelectorAll('.delete_todo');

                 //event.target.style.display = 'none';

let data_id = data.split('|')[0].trim();
let data_message = data.split('|')[1].trim();
let messae_html = document.getElementById('msg_html');
y.forEach( (item, index, array) => {
   if (item.getAttribute('data-todo-id') == data_id) {
        item.parentNode.style.background = 'gold';
        item.parentNode.style.display = 'none';
        messae_html.innerHTML = `<div class="alert alert-info">            <strong> ${data_message} </strong>
                <span class="closebtn" style="float:right;background-color:red;color:white;padding:2px;width:25px;text-align:center;margin-bottom:26px;font-size:1em;cursor:pointer;font-weight:bold;border:2px solid white;border-radous:8%;">&times;</span>
                </div>`;
                var close = document.getElementsByClassName("closebtn");
                var i;

                for (i = 0; i < close.length; i++) {
                  close[i].onclick = function(){
                    var div = this.parentElement;
                    div.style.opacity = "0";
                    setTimeout(function(){ div.style.display = "none"; }, 600);
                  }
                }

        //alert(item.getAttribute('data-todo-id')) <span class="alert alert-info">:</span>
   }
} )



               }

    });
  })




});
