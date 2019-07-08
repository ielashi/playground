import In3Client from 'in3'
const Web3 = require('web3');

// use the In3Client as Http-Provider
const web3 = new Web3(new In3Client({
  proof: 'standard',
  signatureCount: 1,
  requestCount: 2,
  chainId: 'mainnet'
}).createWeb3Provider())

// use the web3
async function main() {
  // Check Vitalik's networth.
  const block = await web3.eth.getBalance('0xab5801a7d398351b8be11c439e05c5b3259aec9b')
  console.log(block);
}

main();
