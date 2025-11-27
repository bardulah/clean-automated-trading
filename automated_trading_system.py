#!/usr/bin/env python3
"""
24/7 Automated Trading System with European Markets
Market-intelligent automation for US and European markets
Complete autonomous trading system with comprehensive testing
"""

import os
import sys
import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Any

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Load environment variables
try:
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
except FileNotFoundError:
    print("❌ .env file not found")

class AutomatedTradingSystem:
    """Complete 24/7 automated trading system with European markets"""
    
    def __init__(self):
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging for the automated system"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('automation.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def get_current_market_status(self) -> str:
        """Determine which markets are currently open"""
        now = datetime.now()
        utc_hour = now.hour
        utc_minute = now.minute
        current_time = utc_hour * 100 + utc_minute
        
        # European markets: 08:00-17:30 UTC
        if 800 <= current_time <= 1730:
            return "EU_MARKETS_OPEN"
        
        # US markets: 16:30-21:00 UTC  
        if 1630 <= current_time <= 2100:
            return "US_MARKETS_OPEN"
            
        # UK markets: 08:00-16:30 UTC
        if 800 <= current_time <= 1630:
            return "UK_MARKETS_OPEN"
            
        return "MARKETS_CLOSED"
    
    def get_market_focus(self, market_status: str) -> str:
        """Get the appropriate market focus based on current status"""
        if market_status == "EU_MARKETS_OPEN":
            return "European markets (ASML, SAP focus)"
        elif market_status == "US_MARKETS_OPEN":
            return "US markets (full coverage)"
        elif market_status == "UK_MARKETS_OPEN":
            return "UK markets"
        else:
            return "Preparation and monitoring mode"
    
    async def run_intelligent_cycle(self) -> Dict[str, Any]:
        """Run a single intelligent trading cycle"""
        try:
            self.logger.info("🚀 Starting intelligent trading cycle")
            
            # Get current market status
            market_status = self.get_current_market_status()
            market_focus = self.get_market_focus(market_status)
            
            self.logger.info(f"📊 Market Status: {market_status}")
            self.logger.info(f"🎯 Focus: {market_focus}")
            
            # Run comprehensive multi-agent system analysis
            from comprehensive_multi_agent_analysis import main as run_comprehensive_analysis
            results = await run_comprehensive_analysis()
            
            # Analyze results
            cycle_results = {
                "timestamp": datetime.now().isoformat(),
                "market_status": market_status,
                "market_focus": market_focus,
                "trading_results": results,
                "next_cycle_recommendation": "Continue monitoring" if market_status == "MARKETS_CLOSED" else "Active trading"
            }
            
            self.logger.info(f"✅ Cycle completed successfully")
            return cycle_results
            
        except Exception as e:
            self.logger.error(f"❌ Cycle failed: {str(e)}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "market_status": self.get_current_market_status()
            }
    
    async def run_continuous_operation(self):
        """Run continuous 24/7 operation"""
        self.logger.info("🌍 Starting 24/7 continuous operation")
        
        while True:
            try:
                market_status = self.get_current_market_status()
                
                if market_status != "MARKETS_CLOSED":
                    self.logger.info(f"⏰ Active trading cycle at {datetime.now()}")
                    await self.run_intelligent_cycle()
                    
                # Wait based on market status
                if market_status == "MARKETS_CLOSED":
                    wait_time = 3600  # 1 hour during closed markets
                else:
                    wait_time = 1800  # 30 minutes during open markets
                    
                self.logger.info(f"😴 Sleeping for {wait_time//60} minutes")
                await asyncio.sleep(wait_time)
                
            except KeyboardInterrupt:
                self.logger.info("🛑 Stopping continuous operation")
                break
            except Exception as e:
                self.logger.error(f"❌ Continuous operation error: {str(e)}")
                await asyncio.sleep(300)  # 5 minutes on error

def main():
    """Main entry point for 24/7 trading automation"""
    system = AutomatedTradingSystem()
    
    print("🤖 24/7 Automated Trading System")
    print("Market-intelligent US and European markets automation")
    print("=" * 60)
    
    # Check if running in continuous mode
    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        print("🔄 Starting continuous 24/7 operation")
        asyncio.run(system.run_continuous_operation())
    else:
        print("🎯 Running single intelligent cycle")
        result = asyncio.run(system.run_intelligent_cycle())
        print(f"✅ System operational: {result.get('market_status', 'Unknown')}")
        
        # Show summary
        if "trading_results" in result:
            print("\n📈 Trading Summary:")
            trading = result["trading_results"]
            if "demo_results" in trading:
                demo = trading["demo_results"]
                print(f"   Demo trades: {len(demo.get('demo_sold', []))} sold, {len(demo.get('demo_bought', []))} bought")
            if "real_actions" in trading:
                print(f"   Real recommendations: {len(trading['real_actions'])}")

if __name__ == "__main__":
    main()
