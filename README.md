# Coingecko Hackathon - Market Prediction with CoinGecko MCP
## Introduction
CoinGecko offers one of the largest and most comprehensive datasets in the crypto space. For this hackathon, my idea is to utilize the CoinGecko MCP to create a fun and engaging prediction market. This could be implemented either as a standalone dApp or as an integrated feature within the CoinGecko app. This would enable users to make real-time predictions on market trends and earn rewards for accurate forecasts. During my research, I explored various crypto analytics platforms and found that none of them offer this type of prediction based user interaction. Therefore, I think that adding such a feature could make CoinGecko more fun and interactive, helping to increase the app’s visibility and boost user engagement.  If implemented as a standalone dApp, It could also be used with smart contracts to vote, automate reward distribution, and generate fee-based revenue for the platform.

## Prototype
I understand that creating such a fully functional application would require significant time and effort. Therefore, I have included a simple prototype that was generated using Claude AI, along with a complete system architecture to demonstrate how the concept could be implemented in practice.

Prototype URL: https://claude.ai/public/artifacts/7a8ab5b6-8256-4a7b-90ff-bcc42f4e4e51 \
*Please ignore the refresh button, as it frequently hits the usage limits of the free Claude LLM and often results in errors. The core idea is that clicking the refresh button would generate a new set of prediction data from the MCP.*

Update on August 8:
Creating a simple python script using smolagent integrate with the OpenAI API and CoinGecko MCP to generate prediction questions. I have attached the code in this repo.
<img width="1155" height="770" alt="image" src="https://github.com/user-attachments/assets/c293858e-1dc9-44b2-930e-d49d53f6ec6c" />

## Architecture Overview
There are two possible solutions: one that operates fully off-chain and another that integrates with the blockchain.
### Step 1: Automated Prediction Generation
A scheduler, integrated with CoinGecko MCP, can automatically generate prediction questions on a daily, weekly, or monthly basis in the backend. I tested this using endpoints like `get_coins_top_gainer_losers`, `get_search_trending`, and `get_new_coins_list`, and the outputs were solid and relevant. These questions can be categorized based on MCP-supported data such as trending tokens, top gainers, top losers, NFTs, newly listed meme tokens, and more. Each prediction will align with a specific timeframe (daily, weekly, or monthly) to keep the content fresh and engaging. A pre-structured LLM prompt system will be required to consistently guide the LLM in generating unique questions.
### Step 2: Voting Mechanism
Users can participate in two ways:
- Free Voting (for Integration into the CoinGecko Application): Registered users on the CoinGecko app receive one free vote per prediction.
- Staked Voting (for standalone application): Users can connect with their crypto wallets and vote by staking USDT or USDC. The staked funds are securely held in a smart contract and remain locked until the prediction event concludes at the predefined timestamp.
### Step 3: User Discussion (Before Prediction Ends)
A discussion section can be introduced to allow users to share their thoughts, making the experience more interactive and community-driven.
### Step 4: Reward Settlement & Distribution
The scheduler runs daily to determine if any prediction events have concluded. Once identified, the system processes the results and distributes rewards based on user participation.
- Off-Chain Flow: The backend verifies user votes against outcomes and automatically distributes CoinGecko Candies to users who answered correctly.
- On-Chain Flow: If integrated with smart contracts, the backend checks which users won. Winners can claim their original staked tokens plus a share of the total pool, which collected from the losing side. Losers forfeit their stake. A small fee (e.g. 1%) can optionally be taken from the reward pool as a platform fee.

The full architecture of the off-chain flow is as follows:
<img width="1081" height="683" alt="image" src="https://github.com/user-attachments/assets/3897f66b-deb2-4eae-b8e3-a11ba0397e20" />

The full architecture of the on-chain flow is as follows:
<img width="1200" height="585" alt="image" src="https://github.com/user-attachments/assets/68ee386f-8a1c-43de-858b-195797f37114" />

Apologies if the diagram is a bit confusing...😅

## Further Improvement
The current design relies solely on MCP-supported data, but it can be enhanced by integrating additional sources, such as news or by allowing the community to submit predictions. This would help diversify the types of questions and make the system more fun to interact.

## Clarification on Submission Validity
I'm not sure if submitting an AI-generated prototype is valid for this hackathon and also that whether designing an idea based on the CoinGecko app is allowed. If either of these is not permitted, please feel free to reach out to me.

