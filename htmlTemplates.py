css = '''
<style>
.chat-message {
    padding: 20px; border-radius: 0.5rem; margin-bottom: 1rem; display: flex; items-align: center;
}
.chat-message.user {
    background-color: #262730
}
.chat-message.bot {
    background-color: #262730
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message-user {
display: flex;
  width: 90%;
  justify-content: right;
  item-align: center;
  padding: 0 1.5rem;
  color: #fff;
}

.chat-message .message-bot {
  width: 90%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/chatbot-3d-icon-download-in-png-blend-fbx-gltf-file-formats--communication-robotic-talk-online-blog-innovation-pack-appliances-icons-5627910.png?f=webp" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message-bot">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message-user">{{MSG}}</div>
    <div class="avatar">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/user-3d-icon-download-in-png-blend-fbx-gltf-file-formats--avatar-profile-man-interface-pack-icons-5209354.png">
    </div>
</div>
'''