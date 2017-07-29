function shiborHandler(){
    //shibor数据的加载 & 画图
    console.log('start shiborHandler');
    var rso=echarts.init(document.getElementById('reportShiborOneNight'));
    var rss=echarts.init(document.getElementById('reportShiborShort'));
    var rsl=echarts.init(document.getElementById('reportShiborLong'));
    $.get("component/shibor/client/ajax/history").done(
        function(data){
                var optionsOneNight={
                    title:{text:'上海银行间同业拆放利率(shibor)走势',subtext:'www.financedatas.com'},
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
                        type:'value',
                        name:'利率',
                        nameLocation:'middle',
                        nameRotate:90,
                        nameGap:30,
                        scale: true,
                        splitArea: {
                            show: true
                        }

                        //name:'利率'
                    },
                    dataZoom:{
                        type:'slider',
                        start:80,
                        end:100
                    },
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
                        type:'value',
                        scale: true,
                        splitArea: {
                            show: true
                        }

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
                        type:'value',
                        scale: true,
                        splitArea: {
                            show: true
                        }

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
    );
}

function glodHandler(){
    // 加载黄金相关的数据
    var rg=echarts.init(document.getElementById('reportGlod'));
    var rgl=echarts.init(document.getElementById('reportGlodLong'));
    $.get("component/glod/client/ajax/history").done(
        function(data){
                var optionsGlod={
                    title:{text:'国内黄金价格近期走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['国内金价']
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
                    /*
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },*/
                    yAxis: {
                        scale: true,
                        splitArea: {
                            show: true
                        }
                    },
                    dataZoom:{
                        type:'slider',
                        start:85,
                        end:100
                    },
                    series:[
                        {
                            name:'国内金价',
                            type:'k',
                            smooth:true,
                            data:data['datas']
                        }
                        
                    ]
                };  

                var optionsGlodLong={
                    title:{text:'国内黄金价格历史走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['国内金价']
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
                    /*
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },*/
                    yAxis: {
                        scale: true,
                        splitArea: {
                            show: true
                        }
                    },
                    dataZoom:{
                        type:'slider',
                        start:0,
                        end:100
                    },
                    series:[
                        {
                            name:'国内金价',
                            type:'k',
                            smooth:true,
                            data:data['datas']
                        }
                        
                    ]
                };
                rg.setOption(optionsGlod);
                rgl.setOption(optionsGlodLong);
        }
    );
}

function pbcHandler(){
    var rp0=echarts.init(document.getElementById('reportPbcM0'));
    var rp1=echarts.init(document.getElementById('reportPbcM1'));  
    var rp2=echarts.init(document.getElementById('reportPbcM2')); 
    $.get("component/pbc/client/ajax/history").done(
        function(data){
                var optionsM0={
                    title:{text:'流通中货币(M0)',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['M0']
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
                    /*
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },*/
                    yAxis: {
                        scale: true,
                        splitArea: {
                            show: true
                        }
                    },
                    dataZoom:{
                        type:'slider',
                        start:85,
                        end:100
                    },
                    series:[
                        {
                            name:'M0',
                            type:'line',
                            smooth:true,
                            data:data['m0']
                        }
                        
                    ]
                };  
                var optionsM1={
                    title:{text:'货币(M1)',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['M1']
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
                    /*
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },*/
                    yAxis: {
                        scale: true,
                        splitArea: {
                            show: true
                        }
                    },
                    dataZoom:{
                        type:'slider',
                        start:0,
                        end:100
                    },
                    series:[
                        {
                            name:'M1',
                            type:'line',
                            smooth:true,
                            data:data['m1']
                        }
                        
                    ]
                };  
                var optionsM2={
                    title:{text:'货币和准货币(M2)',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['M2']
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
                    /*
                    yAxis:{
                        type:'value'
                        //name:'利率'
                    },*/
                    yAxis: {
                        scale: true,
                        splitArea: {
                            show: true
                        }
                    },
                    dataZoom:{
                        type:'slider',
                        start:0,
                        end:100
                    },
                    series:[
                        {
                            name:'M2',
                            type:'line',
                            smooth:true,
                            data:data['m2']
                        }
                        
                    ]
                };

                rp0.setOption(optionsM0);
                rp1.setOption(optionsM1);
                rp2.setOption(optionsM2);
        }
    );
}

document.getElementById('shiborItem').addEventListener('click',function(){
    shiborHandler();
});
document.getElementById('glodItem').addEventListener('click',function(){
    glodHandler();
});
document.getElementById('pbcItem').addEventListener('click',function(){
    pbcHandler();
});
shiborHandler();
