from django.http import JsonResponse
import asyncio

def sync_view(request):
    """Traditional synchronous view."""
    return JsonResponse({"message": "This is a synchronous WSGI view!"})

async def async_view(request):
    """Modern asynchronous view."""
    await asyncio.sleep(1)  # Simulate I/O bound task
    return JsonResponse({"message": "This is an asynchronous ASGI view!"})
