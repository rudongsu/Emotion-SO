select mo as "Month",
  max(case when tag = 'flutter' then total end) as Flutter,
  max(case when tag = 'react-native' then total end) as "React Native",
  max(case when tag = 'angularjs' then total end) as AngularJS,
  max(case when tag = 'vue.js' then total end) as VueJS,
  max(case when tag = 'xamarin' then total end) as Xamarin,
  max(case when tag = 'cordova' then total end) as Cordova,
  max(case when tag = 'ionic-framework' then total end) as Ionic
from (
  select
    format(p.CreationDate, 'MMM yyyy') as mo,
    t.TagName as tag,
    count(p.id) as total
  from
    Posts p
    inner join PostTags pt on p.Id = pt.PostId
    inner join Tags t on t.Id = pt.TagId
  where
    p.CreationDate > '2020-01-01' AND p.CreationDate < '2020-06-01' AND
    (
      t.TagName = 'flutter'
      or t.TagName = 'react-native'
      or t.TagName = 'angularjs'
      or t.TagName = 'vue.js'
      or t.TagName = 'xamarin'
      or t.TagName = 'cordova'
      or t.TagName = 'ionic-framework'
    )
  group by
    format(p.CreationDate, 'MMM yyyy'),
    t.TagName
) q
group by mo
order by convert(DateTime, mo, 101)
