function shiborHandler(){
    //shibor数据的加载 & 画图
    console.log('start shiborHandler');
    var rso=echarts.init(document.getElementById('reportShiborOneNight'));
    var rss=echarts.init(document.getElementById('reportShiborShort'));
    var rsl=echarts.init(document.getElementById('reportShiborLong'));
    $.get("http://www.workstudio.com/component/shibor/client/ajax/history").done(
        function(data){
                var optionsOneNight={
                    title:{text:'上海银行间同业拆放利率(shibor)隔夜走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['隔夜']
                    },
                    grid:{left:'6%'},
                    toolbox: {
                        show: true,
                        feature: {
                            magicType: {show: true, type: ['stack', 'tiled']},
                            saveAsImage: {show: true}
                    }
                    },
                    xAxis:{
                        type:'category',
                        boundaryGap: false,
                        data:data['pushDate'],
                        name:'日期'
                    },
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },
                    dataZoom:{type:'slider'},
                    series:[
                        {
                            name:'隔夜',
                            type:'line',
                            smooth:true,
                            data:data['oneNight']
                        }
                        
                    ]
                };
                var optionsShort={
                    title:{text:'上海银行间同业拆放利率(shibor)走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['一周','两周','一月']
                    },
                    grid:{left:'6%'},
                    toolbox: {
                        show: true,
                        feature: {
                            magicType: {show: true, type: ['stack', 'tiled']},
                            saveAsImage: {show: true}
                    }
                    },
                    xAxis:{
                        type:'category',
                        boundaryGap: false,
                        data:data['pushDate'],
                        name:'日期'
                    },
                    yAxis:{
                        type:'value'
                    },
                    dataZoom:{type:'slider'},
                    series:[
                        {
                            name:'一周',
                            type:'line',
                            smooth:true,
                            data:data['oneWeek']
                        },
                        {
                            name:'两周',
                            type:'line',
                            smooth:true,
                            data:data['twoWeek']                           
                        },
                        {
                            name:'一月',
                            type:'line',
                            smooth:true,
                            data:data['oneMonth']                           
                        }
                        
                    ]

                };
                var optionsLong={
                    title:{text:'上海银行间同业拆放利率(shibor)走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['三月','六月','九月','一年']
                    },
                    grid:{left:'6%'},
                    toolbox: {
                        show: true,
                        feature: {
                            magicType: {show: true, type: ['stack', 'tiled']},
                            saveAsImage: {show: true}
                    }
                    },
                    xAxis:{
                        type:'category',
                        boundaryGap: false,
                        data:data['pushDate'],
                        name:'日期'
                    },
                    yAxis:{
                        type:'value'
                    },
                    dataZoom:{type:'slider'},
                    series:[
                        {
                            name:'三月',
                            type:'line',
                            smooth:true,
                            data:data['threeMonth']
                        },
                        {
                            name:'六月',
                            type:'line',
                            smooth:true,
                            data:data['sixMonth']                           
                        },
                        {
                            name:'九月',
                            type:'line',
                            smooth:true,
                            data:data['nineMonth']                           
                        },
                        {
                            name:'一年',
                            type:'line',
                            smooth:true,
                            data:data['oneYear']                           
                        }                        
                    ]

                };
                rso.setOption(optionsOneNight);
                rss.setOption(optionsShort);
                rsl.setOption(optionsLong);
        }
    )
}

document.getElementById('shiborItem').addEventListener('click',function(){
    shiborHandler();
});
shiborHandler();
