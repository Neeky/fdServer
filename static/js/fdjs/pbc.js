
function pbcHandler(){
    var rpms=echarts.init(document.getElementById('reportPbcMS'));
    var rp0=echarts.init(document.getElementById('reportPbcM0'));
    var rp1=echarts.init(document.getElementById('reportPbcM1'));  
    var rp2=echarts.init(document.getElementById('reportPbcM2')); 
    $.get("component/pbc/get/latest/money/supply").done(
        function(datas){
                var optionsMS={
                    title:{text:'央行货币供应量构成比例',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'item'},
                    grid:{left:'6%'},
                    series:[
                        {
                            name:'货币供应量',
                            type:'pie',
                            radius : '55%',
                            center: ['50%', '50%'],
                            data:[
                                {value:datas['m0'],name:'流通中的货币(m0)'},
                                {value:datas['m1'],name:'货币(m1)'},
                                {value:datas['m2'],name:'货币和准货币(m2)'}
                            ]
                        }
                        
                    ]
                };  
                rpms.setOption(optionsMS);
        }
    );

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

