from pyoptimum import Client
from functions.portfolio_object import PortfolioDataObject

print('PyOptimum Porfolio Example for Website')
print('> Pulling data from Yahoo Finance')
# setup problem


ticker_list = ['SPY','MINT']

prt = PortfolioDataObject(ticker_list)

# covariance calculated from historical data
Q = prt.covariance_matrix.values.tolist()

# returns calculated from historical data
r = prt.calc_return.tolist()

# beginning of Mauricio's original example
# initial holdings
x0 = [.1, .7]

# cashflow
cashflow = 1

# expected return
mu = .08

# bundle data
data = {
    'Q': Q,
    'r': r,
    'x0': x0,
    'mu': mu,
    'cashflow': cashflow
}

print('> Initializing client')
# initialize a client to connect to the api
username = 'demo@optimize.vicbee.net'
password = 'optimize'
client = Client(username=username, password=password)

print('> Calling API')
# make a call to the api
result = client.call('portfolio', data)

print('> Got solution')
print('  status = {}'.format(result['status']))
print('  portfolio return = {}'.format(mu))
print('  portfolio variance = {}'.format(result['obj']))
print('  positions = {}'.format(result['x']))
print('  Nice!  I hope you make more money!')
