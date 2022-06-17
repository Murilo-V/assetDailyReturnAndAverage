def daily_return(asset_name, *daily_closed_prices):
    x=0
    daily_return_lst=[]
    while x<len(daily_closed_prices)-1:
        daily_return_lst.append(round((daily_closed_prices[x+1]-daily_closed_prices[x])/daily_closed_prices[x]*100,2))
        x+=1
    average_daily_return = sum(daily_return_lst)/len(daily_return_lst)
    print('Os retornos diários (%) do ativo '+asset_name +' foram: '+str(daily_return_lst))
    print('A média de retorno diário (%) do ativo '+asset_name+' foi de: '+str(average_daily_return))

# exemplo de retorno diário e média do fundo imobiliário KNRI11
# daily_return('KNRI11',*[132.93, 131.75, 131.08, 131.64, 131.50])