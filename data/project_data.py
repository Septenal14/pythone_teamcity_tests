from utils.faker import DataGenerator


class ProjectData:
    @staticmethod
    def create_project():
        return {
            "parentProject": {"locator": "_Root"},
            "name": DataGenerator.generate_project_name(),
            "id": DataGenerator.generate_project_id(),
            "copyAllAssociatedSettings": True
        }
