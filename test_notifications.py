#!/usr/bin/env python3
"""Test notifications system"""

import asyncio
from src.unified_trading.orchestration.notification_system import NotificationSystem

async def test_notifications():
    """Test the notification system"""
    system = NotificationSystem()
    await system.send_trading_alert("Test notification from automated system")
    print("✅ Notification test completed")

if __name__ == "__main__":
    asyncio.run(test_notifications())
