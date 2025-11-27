# 24/7 Automated Trading System

🤖 **Complete 24/7 automated trading system with European markets focus**

## 🚀 Features

### ✅ **Verified European Markets Integration**
- **ASML_US_EQ**: ASML Holding NV (Semiconductor equipment leader)
- **SAP_US_EQ**: SAP SE (Enterprise software)
- **22+ additional European companies** with verified Trading 212 availability
- **Market-intelligent scheduling**: Focuses on European markets when US markets are closed

### ✅ **24/7 Global Market Coverage**
- **US Markets**: 16:30-21:00 UTC (9:30 AM-4:00 PM EST)
- **European Markets**: 08:00-17:30 UTC (8:00 AM-5:30 PM CET)  
- **UK Markets**: 08:00-16:30 UTC (8:00 AM-4:30 PM GMT)
- **Result**: True continuous 24/7 operation across global time zones

### ✅ **Production-Ready Automation**
- **Background systemd service integration** for 24/7 operation
- **Automated start/stop** based on market hours
- **Error recovery and health monitoring**
- **Rate limit management** for API optimization
- **Crash recovery** with automatic restart

### ✅ **Real-Time Notifications**
- **Email notifications** to configured recipients
- **Telegram alerts** for instant updates
- **Real-time trading signals** and market timing
- **Risk management warnings**
- **Position tracking updates**

### ✅ **Demo Trading System**
- **Verified SELL order execution** (confirmed Order ID 40700064295)
- **BUY orders** for existing positions
- **Live position tracking** (6 active positions verified)
- **Safety controls** and compliance monitoring

## 📋 Quick Start

### Run Single Intelligent Cycle
```bash
python3 automated_trading_system.py
```

### Test Notification System
```bash
python3 test_notifications.py
```

### Background Service Setup
See `AUTOMATION_SYSTEM_GUIDE.md` for complete systemd integration

## 📚 Documentation

- `AUTOMATION_SYSTEM_GUIDE.md` - Complete automation setup guide
- `NOTIFICATION_GUIDE.md` - Notification system configuration
- `test_notifications.py` - Notification system testing

## 🌍 Market Coverage

The system intelligently switches focus based on market hours:
- **US Market Hours**: Focus on US markets
- **European Hours**: Focus on European markets  
- **Off Hours**: Background monitoring and preparation

## 🔐 Security & Production

- **Environment-based configuration** (no hardcoded credentials)
- **Rate limit protection** for API usage
- **Comprehensive error handling**
- **Production-ready logging and monitoring**

---

**FROM**: Manual trading → **TO**: Full 24/7 automated system with European markets support
