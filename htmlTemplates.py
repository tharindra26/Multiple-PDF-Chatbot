css = '''
<style>
.chat-message{
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-message.user{
    background-color: #2b313e;
}
.chat-message.bot{
    background-color: #475063;
}
.chat-message .avatar{
    width: 15%;
}
.chat-message .avatar img{
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message{
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwh_G_jsYccpZ1E_WC_48tq_Y_6Q-KqRyY7ByqmiRyZA&s">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://ps.w.org/simple-user-avatar/assets/icon-256x256.png?rev=2413146">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''