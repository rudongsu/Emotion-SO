select distinct body
  from posts p
  inner join posttags pt on pt.postid = p.id
  inner join tags t on pt.tagid = t.id
  where t.tagname in ('flutter') 
