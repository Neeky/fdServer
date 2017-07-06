function shiborHandler(){
    //shibor数据的加载 & 画图
    console.log('start shiborHandler');
    var rso=echarts.init(document.getElementById('reportShiborOneNight'));
    $.get("http://www.workstudio.com/component/shibor/client/ajax/history").done(
        function(data){
                var options={
                    title:{text:'上海银行间同业拆放利率(shibor)走势',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['隔夜','一周','两周']
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
                        data:data['pushDate']
                    },
                    yAxis:{
                        type:'value'
                    },
                    series:[
                        {
                            name:'隔夜',
                            type:'line',
                            smooth:true,
                            data:data['oneNight']
                        },
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
                    ]
                };
                rso.setOption(options);
        }
    )
}

document.getElementById('shiborItem').addEventListener('click',function(){
    shiborHandler();
});
shiborHandler();
