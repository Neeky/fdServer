function displayCninfoIndustryInfo(){
    // 加载上市公司信息
    var rci=echarts.init(document.getElementById('reportCninfoIndustry'));
    //var rgl=echarts.init(document.getElementById('reportGlodLong'));
    $.get("component/cninfo/list/company/by/industry").done(
        function(data){
                console.log(data);
                var optionsCninfoIndustry={
                    title:{text:'沪深两市上市公司行业分布',subtext:'www.financedatas.com'},
                    tooltip:{trigger:'axis'},
                    legend: {
                        data:['沪深两市上市公司行业分布']
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
                        data:data['industrys'],
                        name:'行业',
                        scale: true,
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
                            name:'沪深两市上市公司行业分布',
                            type:'bar',
                            smooth:true,
                            data:data['counters']
                        }
                        
                    ]
                };  
                rci.setOption(optionsCninfoIndustry);
        }
    );
}

document.getElementById('stockItem').addEventListener('click',function(){
    //alter('this is stockItem');
    displayCninfoIndustryInfo();
});
