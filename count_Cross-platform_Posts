select distinct count (*) body
  from posts p
  inner join posttags pt on pt.postid = p.id
  inner join tags t on pt.tagid = t.id
  where     (
      t.TagName = 'flutter'
      or t.TagName = 'react-native'
      or t.TagName = 'angularjs'
      or t.TagName = 'vue.js'
      or t.TagName = 'xamarin'
      or t.TagName = 'cordova'
      or t.TagName = 'ionic-framework'
    ) AND
  p.CreationDate < '2020-01-01'
