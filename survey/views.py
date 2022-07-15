from django.shortcuts import render
from django.shortcuts import redirect
from.models import *

import pandas as pd
from sklearn.neighbors import NearestNeighbors
# Create your views here.

def similar(similar_id, matrix, k):
    model_knn = NearestNeighbors(metric='correlation', algorithm='brute')  # 피어슨 유사도 계산
    model_knn.fit(matrix)  # 모델 학습
    query_index = matrix.index.get_loc(similar_id)  # 유사도 대상 쿼리 인덱스

    KN = matrix.iloc[query_index].values.reshape(1, -1)
    distances, indices = model_knn.kneighbors(KN, n_neighbors=k)  # 인접한 k개의 sample에 대한 거리 index 반환
    Rec_similar = list()  # 유사 아이디 저장
    similar_dis = list()  # 유사 거리 저장

    for i in range(1, len(distances.flatten())):  # 유사 리스트 개수만큼 반복
        Rec_similar.append(matrix.index[indices.flatten()[i]])  # 유사 아이디 리스트 저장
        similar_dis.append(distances.flatten()[i])  # 유사 거리 리스트 저장
    return Rec_similar  # 유사한 리스트 반환

def landing(request):
    return render(

        request,
        'survey/index.html',
    )
def submit(request):
    if request.method == 'POST':
        print("post 성공")
        print(request.POST)

        if request.POST.getlist('q1', "") :
            for i in request.POST.getlist('q1', ""):
                print(request.POST.get('name', ""), request.POST.get('age', ""), i, 1)
                Survey.objects.create(user=request.POST.get('name', ""), age=request.POST.get('age', ""), survey=i,
                                      survey_num=1)

        if request.POST.getlist('q2', "") :
            for i in request.POST.getlist('q2', ""):
                print(request.POST.get('name', ""), request.POST.get('age', ""), i, 1)
                Survey.objects.create(user=request.POST.get('name', ""), age=request.POST.get('age', ""), survey=i,
                                      survey_num=1)

        if request.POST.getlist('q3', "") :
            for i in request.POST.getlist('q3', ""):
                print(request.POST.get('name', ""), request.POST.get('age', ""), i, 1)
                Survey.objects.create(user=request.POST.get('name', ""), age=request.POST.get('age', ""), survey=i,survey_num=1)
        #Survey.objects.create(user=request.name, age=request.age,survey = )

        return redirect('/')

def result(request):

    similar_user = []

    br = Survey.objects.filter()
    q1 = br.values('user', 'age', 'survey', 'survey_num')
    rating_data = pd.DataFrame.from_records(q1)
    print(rating_data)
    rating_matrix = rating_data.pivot_table(index='user', columns='survey', values='survey_num')  # 피봇 테이블 생성
    rating_matrix = rating_matrix.fillna(0)
    print(rating_matrix)

    users = rating_data['user'].drop_duplicates()
    print(users)


    if request.method == 'POST':
        print("post 성공")
        print(request.POST)
        choice_name = request.POST.get('month', "")


        similar_user = similar(choice_name, rating_matrix, 4)  # 유사 사용자
        print("유사 사용자 결과",similar_user)
    return render(

        request,
        'survey/result.html',
        {
            'users': users,
            'list': similar_user

        }
    )