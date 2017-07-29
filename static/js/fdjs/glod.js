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

document.getElementById('glodItem').addEventListener('click',function(){
    glodHandler();
});
