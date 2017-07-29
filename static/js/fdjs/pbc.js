
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

document.getElementById('pbcItem').addEventListener('click',function(){
    pbcHandler();
});

