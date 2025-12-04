from db2 import add_user , cleanup_results ,get_user_by_iin

#name, iin, score, time, wrong
# Добавить пользователя
results = get_user_by_iin("456745674567")
for r in results:
    print(r)
