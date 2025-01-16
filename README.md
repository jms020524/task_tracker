# Task Tracker CLI

Task Tracker CLI는 CLI를 통해서 작업을 관리하는 간단한 애플리케이션입니다.

## 기능
- 작업 추가
- 작업 목록 확인
- 작업 업데이트
- 작업 삭제
- 작업 상태 변경

## 사용 방법

### 작업 추가
```bash
python task_cli.py add "Buy grocereis"
```

### 작업 목록 확인
```bash
python task_cli.py list
```

### 작업 업데이트
```bash
python task_cli.py update 1 "Buy grocereis and cook dinner"
```

### 작업 삭제
```bash
python task_cli.py delete 1
```

### 작업 상태 변경
```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```


### 설치 및 실행
1. Python 설치
2. 프로젝트 디렉토리 생성 및 이동
3. task_cli.py 파일 생성 및 코드 작성
4. 명령어를 사용해 작업 관리