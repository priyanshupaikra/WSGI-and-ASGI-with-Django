from django.shortcuts import render
from django.http import JsonResponse
import asyncio

def index_view(request):
    """Serve the two-sided frontend."""
    return render(request, 'chat/index.html')

def sync_view(request):
    """Traditional synchronous view with MongoDB data."""
    from .db import get_latest_messages_sync
    messages = get_latest_messages_sync()
    
    formatted_messages = []
    for m in messages:
        formatted_messages.append({
            "user": m.get("sender_id", "Anonymous"),
            "receiver": m.get("receiver_id", "Broadcast"),
            "message": m.get("message"),
            "timestamp": str(m.get("timestamp"))
        })

    return JsonResponse({"mongo_history": formatted_messages})

def get_users(request):
    """API to fetch all unique senders."""
    from .db import get_all_users_sync
    users = get_all_users_sync()
    return JsonResponse({"users": users})

def get_thread(request):
    """API to fetch specific chat between two people."""
    from .db import get_chat_thread_sync
    u1 = request.GET.get('u1')
    u2 = request.GET.get('u2')
    messages = get_chat_thread_sync(u1, u2)
    
    history = [{
        "sender": m.get("sender_id"),
        "message": m.get("message"),
        "timestamp": str(m.get("timestamp"))
    } for m in messages]
    
    return JsonResponse({"history": history})

async def async_view(request):
    """Modern asynchronous view."""
    await asyncio.sleep(1)  # Simulate I/O bound task
    return JsonResponse({"message": "This is an asynchronous ASGI view!"})
