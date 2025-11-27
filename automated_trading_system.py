#!/usr/bin/env python3
"""
24/7 Automated Trading System with European Markets
Market-intelligent automation for US and European markets
"""

import os
import sys
import asyncio
from datetime import datetime

sys.path.insert(0, 'src')

from automated_trading_system import AutomatedTradingSystem

def main():
    """Main entry point for 24/7 trading automation"""
    system = AutomatedTradingSystem()
    
    print("🤖 24/7 Automated Trading System")
    print("Market-intelligent US and European markets automation")
    
    # Run single intelligent cycle
    result = asyncio.run(system.run_intelligent_cycle())
    print(f"✅ System operational: {result}")

if __name__ == "__main__":
    main()
