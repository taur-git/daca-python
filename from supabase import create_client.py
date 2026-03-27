from supabase import create_client
 
# Asenda oma Supabase andmetega (Connect > API Keys)
url = "https://jhyshxhaazlstyjjamqz.supabase.co"
key = "sb_publishable_ybVINCJTb8_6ztEM91ZZRw_VGb7cw0l"
 
supabase = create_client(url, key)
 
# Asenda oma tabeli nimega (nt 'test_sales' või 'team_members')
response = supabase.table('team_members').select("*").execute()
 
print(f"Leitud ridu: {len(response.data)}")
for row in response.data:
    print(row)